# url-video-player-experiment2 (public)

This is NOT the original source code of the app.

## Contents
`releases/` (phone APKS + SHA256SUMS), `patch/` (the change), `decoded-patched-base/decoded-patched-base.zip` (apktool decode of the patched base.apk). Phone APKS SHA256: 3d0409d2e16418597e43e206e689aa7838bd612ba8e003ec77955764ed2882f0.

## What this is
- The app is a third-party Android video player, package `info.t4w.vp`, version 4.0, build 413. No original project (Gradle, Java or Kotlin source) was ever available. It was never written or owned by the repo owner.
- `releases/` holds the phone build (experiment2) the owner tested and approved on Nov 23, 2026: `UrlVideoPlayer-4.0-experiment2-original-resources-48ff7a73.apks` (7,732,958 bytes, SHA256 in `SHA256SUMS`). It has the base APK plus ar, arm64_v8a, en and xhdpi splits.
- `patch/changes.patch` is the small change that makes experiment2: it redirects 3 ad-request calls in `VideoPlayer.smali` and `sPos9472.smali` to the existing no-ad callback. `patch/patch_narrow.py` is the script that applied it to a decoded tree.
- `decoded-patched-base/decoded-patched-base.zip` is an apktool decode (smali code and resources) of the patched `base.apk` from that same build. The patch is already applied in it. It is a decompile for reference, not original source, and it was not rebuilt or tested from this tree.

## Modified ad-removal build (v2, testing)
`releases/update-4.0-noads-v2-modified-ad-removal-unofficial.apk` (20,694,726 bytes, SHA256 dce316adf9356fb9e930e4e3220330f957f7d8eb12f05163612f5b19e37062d5) is a modified build of the third-party app update.apk (info.t4w.vp 4.0, build 413). It is NOT an official release. It removes ad requests in the ad loader so no ad is requested. It is signed with a new key, so it does not update over earlier builds (uninstall first). Static checks only: it has not been tested on a device yet, and it is not confirmed that movies and series play in it.

## Not included
- No signing keys or passwords. The build is signed with a trial key that is not stored here.
- No TV (ARM32) variant. It was a later build and was never tested.
- No third-party ad-free mod and no unpatched original APK.
- No Ostora frontend trials.

## Notes
- Only the owner tested the phone build. Nobody else tested it.
- Rebuilding from the decoded tree needs apktool and a new signing key.
