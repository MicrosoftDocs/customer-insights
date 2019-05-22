from __future__ import absolute_import, print_function

import time

from aria import LogManager, Logger, EventProperties, PiiKind


def main():
    # Step 0. Initialize the logger
    # =================================
    # Here we're not using any special config options, accepting the LogManager defaults.
    # Feel free to change the tenant token to one you created so you can play around with
    # the events some more in the portal. See https://portal.aria.ms
    logger = LogManager.initialize('de9e11652d4c466c92710be0b8c8f857-86e9f47c-555b-48b2-9b0b-247978533b5e-7176')

    # Here is a demo of how to log a basic event
    demo_basic_logging(logger)

    # Here's a demo of applying context to a logger.
    # This lets us apply some basic properties to ALL events logged to our Logger.
    demo_contextual_logging(logger)

    # Here's a demo of adding event subscribers to keep track of logged events.
    # We first flush the LogManager so that the only events this demo sees are
    # events logged in the demo itself, and not events still waiting around in
    # the SDK pipeline.
    LogManager.flush()
    demo_log_manager_subscribers(logger)

    # This is a demo of the logging speed of the Python SDK. It times how long
    # it takes to log 2000 events and flush them all.
    demo_logging_speed(logger)

    # Lastly, we must call LogManager.flush() before exiting so we ensure that everything gets
    # uploaded, and LogManager.tear_down() to shut down the telemetry system cleanly. For
    # convenience, there is LogManager.flush_and_tear_down(), which does both of these.
    LogManager.flush_and_tear_down(30)


def demo_basic_logging(logger):
    # type: (Logger) -> None

    # First, we log an empty event using just an event name
    logger.log_event('basic_empty_event')

    # Here we'll log a more complex event.
    # This creates an event with the name 'basic_event', and fills out its values
    # =================================
    event = EventProperties('basic_event')

    event.set_property('rpm', 42)
    event.set_property('device_name', 'Test Device 9001')
    event.set_property('active', True)
    event.set_property('temperature_c', 20.7)

    # Setting personally identifiable information - this will be rendered opaque / unreadable, and
    # no longer personally identifiable upon uploading.
    event.set_property('username', 'myCoolUsername42', pii_kind=PiiKind.PiiKind_DistinguishedName)
    event.set_property('device_ip', '127.0.0.1', pii_kind=PiiKind.PiiKind_IPv4Address)

    # Now let's upload the event!
    # =================================
    logger.log_event(event)


def demo_contextual_logging(logger):
    # type: (Logger) -> None

    # First, let's set a global context property. This means that every Logger we get will have
    # these properties set out. This even applies retroactively, so our existing logger will be
    # updated, and its context will include this event.
    LogManager.set_context('device_series_major', 'Test Device 9x')

    # Now, let's set a local context property. This applies only to this specific logger, so other
    # Loggers created by our LogManager will be unaffected.
    logger.set_context('device_series_minor', '001')

    # Now let's log an "empty" event. It will actually include the contexts we set for both the
    # LogManager and the logger.
    # Note that if we log an actual event, then the uploaded event will have properties from both
    # the context and the event we logged.
    logger.log_event('contextual_empty_event')

    # If both a LogManager and one of its Loggers set the same context, then the logger's context
    # overrides the LogManager's context. Likewise, a property in the logged event can override
    # one in a Logger's context. The general priority, from least to most important, is like this:
    # LogManager > Logger > Logged Event
    event = EventProperties('contextual_empty_event')
    event.set_property('device_series_minor', '002')

    logger.log_event(event)

    # This clears the context so it won't apply to any later demos.
    logger.clear_context()
    LogManager.clear_context()


def demo_log_manager_subscribers(logger):
    # type: (Logger) -> None

    # First, declare a subscriber function. It should take 3 arguments:
    # A string tenant, a list of int event IDs, and the int status code.
    # Each id in ids should correspond to an id returned by the logger.log_event()
    # function.
    #
    # If status is > 0, then it's an HTTP status code received from uploading
    # the events. 200 if it's successful, not 200 otherwise.
    # If the status is < 0, then it's an error code for an error that happened
    # before the event was uploaded.
    def subscriber(tenant_token, ids, status):
        # type: (str, List[int], int) -> None
        print('Subscriber callback for tenant ' + tenant_token)
        print('ids: ' + str(ids))
        print('status: ' + str(status))
        print('')

    # We add the subscriber to the LogManager. Now we'll get feedback whenever
    # a group of events leaves the Pipeline.
    LogManager.add_subscriber(subscriber)

    # Log a few empty events to have something for the callback to listen to.
    for _ in range(10):
        logger.log_event('basic_empty_event')

    # Flush the pipeline, ensuring events are either dropped or uploaded and
    # causing the subscriber to be called.
    LogManager.flush()

    # Cleaning up subscribers at the end.
    LogManager.clear_subscribers()


def demo_logging_speed(logger):
    # type: (Logger) -> None

    # First, we time how long it takes to log 1000 empty events.
    start = time.time()
    for _ in range(1000):
        logger.log_event('basic_empty_event')
    mid_empty = time.time()

    # Here, we're creating a complex event to log.
    event = EventProperties('basic_event')
    event.set_property('rpm', 38)
    event.set_property('device_name', 'Test Device 9001')
    event.set_property('active', False)
    event.set_property('temperature_c', 12.34)

    # Now, we're timing how long it takes to log 1000 complex events.
    for _ in range(1000):
        logger.log_event(event)

    mid_complex = time.time()

    # Last, we flush the pipeline and record how long it takes to flush.
    # Once flush() has returned, the pipeline should be empty.
    LogManager.flush()
    end = time.time()

    # And now we print the results
    print('Logged 1000 empty events in {time:3.3f}s'.format(time=mid_empty - start))
    print('Logged 1000 complex events in {time:3.3f}s'.format(time=mid_complex - mid_empty))
    print('Flushed all events in {time:3.3f}s'.format(time=end - mid_complex))
    print('Total time: {time:3.3f}s'.format(time=end - start))
    print('')


if __name__ == '__main__':
    main()
