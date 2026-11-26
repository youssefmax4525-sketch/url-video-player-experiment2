# url-video-player-experiment2 (private)

This is NOT the original source code of the app.

## Status
Only the README and `patch/` are in this repo so far. The browser upload of binary files failed, so `releases/` and `decoded-patched-base/` described below are NOT uploaded yet. Their SHA256 (phone APKS): 3d0409d2e16418597e43e206e689aa7838bd612ba8e003ec77955764ed2882f0.

## What this is
- The app is a third-party Android video player, package `info.t4w.vp`, version 4.0, build 413. No original project (Gradle, Java or Kotlin source) was ever available. It was never written or owned by the repo owner.
- `releases/` holds the phone build (experiment2) the owner tested and approved on Nov 23, 2026: `UrlVideoPlayer-4.0-experiment2-original-resources-48ff7a73.apks` (7,732,958 bytes, SHA256 in `SHA256SUMS`). It has the base APK plus ar, arm64_v8a, en and xhdpi splits.
- `patch/changes.patch` is the small change that makes experiment2: it redirects 3 ad-request calls in `VideoPlayer.smali` and `sPos9472.smali` to the existing no-ad callback. `patch/patch_narrow.py` is the script that applied it to a decoded tree.
- `decoded-patched-base/decoded-patched-base.zip` is an apktool decode (smali code and resources) of the patched `base.apk` from that same build. The patch is already applied in it. It is a decompile for reference, not original source, and it was not rebuilt or tested from this tree.

## Not included
- No signing keys or passwords. The build is signed with a trial key that is not stored here.
- No TV (ARM32) variant. It was a later build and was never tested.
- No third-party ad-free mod and no unpatched original APK.
- No Ostora frontend trials.

## Notes
- Only the owner tested the phone build. Nobody else tested it.
- Rebuilding from the decoded tree needs apktool and a new signing key.
