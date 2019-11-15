---
uid: developers/downloads/ingest
title: Getting started with the CSV Sender
author: ruthaisabokhae
description: Getting started with the Event Sender
ms.author: ruthai
ms.date: 08/27/2019
ms.service: product-insights
ms.topic: conceptual
---
# Getting started with the event sending tool
The event sending tool can be used to send both CSV and Key/Value Pair formatted signals to Product Insights.


## Download the event sending tool
Depending on your Operating System, you should download one of the following command-line executables:

* [Windows](https://download.pi.dynamics.com/sdk/ProductInsightsSenders/EventSender/Windows/pi.exe)
* [Linux](https://download.pi.dynamics.com/sdk/ProductInsightsSenders/EventSender/Linux/pi)
* [macOS](https://download.pi.dynamics.com/sdk/ProductInsightsSenders/EventSender/macOS/pi)


## Get your ingestion key
You can find the ingestion key for your Product Insights tenant on its settings page. [Here is how to find and copy your key.](api-token.md)


## Log an event

### Log a CSV file
With an open terminal in the same directory as the downloaded sender, run the following command to upload a CSV file.

```bash
$ pi -t <ingestion_key> -s <signal_name> -f csv - 1st_file.csv 2nd_file.csv ... nth_file.csv
```

When uploading CSVs, the only required arguments are `-t` and the `- filenames...` options. If a signal name is provided, then all events get uploaded with the same signal name. If no signal name is provided, then a unique name will be generated for each detected signal following the pattern `signal_<hash>` (e.g. `signal_a4640af933fa4342`).

Be sure to replace `<ingestion_key>` with your actual Product Insights ingestion key and `your_nth_file.csv` with the filename of your CSV file.


### Log key/value pairs
When logging key/value pairs, a signal name must be provided and there must be as many keys as values provided. To log an event with a terminal open, run the following command:
```bash
$ pi -t <ingestion_key> -s <signal_name> some_key "some value" my_int 42 some_cool_value false
``` 

In addition to generating an event from program arguments, it can also use stdin:
```bash
$ echo 'some_key "some value" my_int 42 some_cool_value false' | pt -t <ingestion_key> -s <signal_name> -
```

While not needed, as it's the default option, the format can be explicitly declared by passing `-f kvp` as an argument. In this case, the event being logged is equivalent to the following JSON object:
```json
{
    "some_key": "some value",
    "my_int": 42,
    "some_cool_value": false
}
```


## Optional arguments
While a full listing of arguments can be read by running `pi -h` (or `pi --help`), and more arguments exist, the following covers some useful or important options.

* `-t <tenant>` or `--tenant <tenant>`: (Required) Sets the Product Insights ingestion key to log events to.

* `-s <signal>` or `--signal <signal>`: (Sometimes required) Sets the signal name to log events as. If not specified, then signal names are generated.

* `--skip <skip>`: Skips the first `<skip>` events before logging any to Product Insights.

    Example: `pi -t <tenant> -f csv --skip 30 - data.csv` (skips the first 30 events).

* `--count <count>`: Limits the number of events that get logged to at most `<count>`.

    Example: `pi -t <tenant> -f csv --count 15 - data.csv` (logs at most 15 events).
