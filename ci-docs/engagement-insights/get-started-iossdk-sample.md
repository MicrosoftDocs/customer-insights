# Run the iOS SDK sample for engagement insights

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

## Prerequisites

- [Xcode 9+](https://developer.apple.com/xcode/downloads/)
- [Ingestion key](get-started-ios.md)

## Run Sample

1. [Download the engagement insights iOS SDK sample](https://download.pi.dynamics.com/sdk/EI-SDKs/ei-ios-sample.zip).
2. Unzip the compressed file `ei-ios-sample.zip`.
4. Open the sample app project in Xcode.
5. In the `EIConfig.plist` file, replace the string `“YOUR-INGESTION-KEY”` in the field `ingestionKey` with your workspace ingestion key from the engagement insights portal under Admin -> Workspace -> Installation Guide.
6. Click **Run** to run the sample project.
7. View the events in your workspace.
