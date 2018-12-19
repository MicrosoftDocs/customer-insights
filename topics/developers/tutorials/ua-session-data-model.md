---
layout: page
title: Session Data Model

---

The Data Model is defined using BOND IDL. Refer to [Bond][0] for more information about BOND. 

```
///////////////////////////////////////////////////////////////////////////////
// **Session State**
//
    
    enum SessionState
    {
        Started = 0,
        Ended = 1,
    }

///////////////////////////////////////////////////////////////////////////////
// Session Duration
//

    enum SessionDuration
    {

        // Bucket for: undefined/invalid
        Undefined = 0,

        // Bucket for: 0s < duration <= 3s
        UpTo3Sec = 1,

        // Bucket for: 3s < duration <= 10s
        UpTo10Sec = 2,

        // Bucket for: 10s < duration <= 30s
        UpTo30Sec = 3,

        // Bucket for: 30s < duration <= 60s
        UpTo60Sec = 4,

        // Bucket for: 1m < duration <= 3m
        UpTo3Min = 5,

        // Bucket for: 3m < duration <= 10m
        UpTo10Min = 6,

        // Bucket for: 10m < duration <= 30m
        UpTo30Min = 7,

        // Bucket for: 30m < duration
        Above30Min = 8,
    }

///////////////////////////////////////////////////////////////////////////////
**Session identifies the current session state**


    struct Session : Microsoft.Applications.Telemetry.Interfaces.Extension
    {
        // The session Id uniquely identifies this session, and is expected
        // to be a GUID.
        // [Required]
        1: string Id;

        // The state value indicates whether this represents the Start or
        // End of the session.
        // [Required]
        2: SessionState State = Started;

        // The duration of the session in seconds.
        // [Required]
        5: uint32 Duration;
        
        // The histogram bucket for the session duration.
        // [Required]
        6: SessionDuration DurationBucket = Undefined;

        // The UTC time on the client when the app was first launched on this
        // device by the user. This is in ISO 8601 format, for example:
        // "2013-09-21T21:55:00.9839095Z"
        // It is not that this value be preserved across App (or OS) uninstall and
        // install operations.
        // [Required]
        10: string FirstLaunchTime; 
    };
```

[0]: http://bond
