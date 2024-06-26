# CHANGELOG



## v0.3.5 (2024-05-04)

### Fix

* fix: exclude bump version commits from CHANGELOG.md ([`66f7297`](https://github.com/helton/hbox/commit/66f7297fcf7ea0fb2f4d5484680dc5aefdd4abb2))


## v0.3.4 (2024-05-04)

### Fix

* fix: set upstream for develop branch before merging main back to it ([`f21c2a1`](https://github.com/helton/hbox/commit/f21c2a1e60fe7376374d878beb244346438f1088))


## v0.3.3 (2024-05-04)

### Fix

* fix: make sure we fetch changes made in main by the bot in semantic release step ([`da53c1c`](https://github.com/helton/hbox/commit/da53c1cff6c17ec76aa77ba8b0adfe699646a75a))


## v0.3.2 (2024-05-04)

### Fix

* fix: define outputs for build-and-release job ([`93e810c`](https://github.com/helton/hbox/commit/93e810c7e471cbc0655be91e62533e0c6c2a007a))

* fix: fetch main branch before push merge ([`c277139`](https://github.com/helton/hbox/commit/c277139447166117b47b4b955c3e7441e4c2042b))


## v0.3.1 (2024-05-04)

### Fix

* fix: fetch develop branch before merging main into it ([`d1c997a`](https://github.com/helton/hbox/commit/d1c997afe0dbe94ca9aeb82e815130ead00e216b))


## v0.3.0 (2024-05-04)

### Chore

* chore: small change to sync and trigger pipeline ([`6beedf3`](https://github.com/helton/hbox/commit/6beedf31698ae0979b754790a161982b0b441573))

### Feature

* feat: add reusable workflows and separate steps that can break to allow rerun ([`75cd33d`](https://github.com/helton/hbox/commit/75cd33d53d1aa604df020314755794a84f34b511))

### Fix

* fix: python-semantic-release requires fetch-depth 0 to access full commit history ([`369c92f`](https://github.com/helton/hbox/commit/369c92f3840fada5660797fe4c0c33dd40f2826e))

* fix: remove code checkout from action.yml ([`6f2958c`](https://github.com/helton/hbox/commit/6f2958c4d39e8fc42b1685fd971c19d2cdc5bea7))

* fix: add shell in steps that require a run command ([`74927c7`](https://github.com/helton/hbox/commit/74927c73ee92c6e6043eab720147a562e675478c))

* fix: remove unused inputs from composite action ([`5571763`](https://github.com/helton/hbox/commit/557176391f8aea864be2cbae721fc18a65827431))

* fix: checkout code before using local composite actions ([`5b88d0a`](https://github.com/helton/hbox/commit/5b88d0a9cfdf57d7e0e1b4afa33c57a1a1ed00be))

* fix: use composite actions instead of reusable workflows ([`fa602d6`](https://github.com/helton/hbox/commit/fa602d6a448dec9cb3b7d99f78de13eb249fc984))

* fix: move workflow to first step call ([`4f590e9`](https://github.com/helton/hbox/commit/4f590e9af0d86ab61e91995f37880a5d8e171e91))

* fix: checkout code before using reusable workflow ([`884ffb7`](https://github.com/helton/hbox/commit/884ffb77595c64ab65d4c2f2584790c4edf71e76))


## v0.2.8 (2024-05-03)

### Fix

* fix: protect branches, but use PAT to bypass via pipeline ([`36dfab6`](https://github.com/helton/hbox/commit/36dfab6919ac7bc6cced1d8eae47816401bfd99e))


## v0.2.7 (2024-05-03)

### Fix

* fix: avoid deprecation warning message for ::set-output ([`26ff5a6`](https://github.com/helton/hbox/commit/26ff5a63b8a8d8df9e35a4c05e3b716d4118d0b1))


## v0.2.6 (2024-05-03)

### Chore

* chore: add check to only update a release if it was published ([`cc4783f`](https://github.com/helton/hbox/commit/cc4783f95d9e35d8d0668311ae074ef938c4689d))

### Fix

* fix: looks like python semantic release does not return the generate version either ([`ff10ac6`](https://github.com/helton/hbox/commit/ff10ac6574abfff3faa6a4068429b12e36c88c38))


## v0.2.5 (2024-05-03)

### Fix

* fix: add upload release assets step because dist_glob_patterns isn&#39;t working ([`e574dab`](https://github.com/helton/hbox/commit/e574dabc865e59a5943579d9a5421383bd5629e8))


## v0.2.4 (2024-05-03)

### Fix

* fix: add merge back to develop ([`4731dbe`](https://github.com/helton/hbox/commit/4731dbeab8f629d4310811348098cb811a9a560a))


## v0.2.3 (2024-05-03)

### Fix

* fix: check if dist files are available to upload ([`b3ffb45`](https://github.com/helton/hbox/commit/b3ffb4568f7783bcebdba9e0531b7a3ab55b805a))


## v0.2.2 (2024-05-03)

### Fix

* fix: check file upload to GitHub release ([`465b5f7`](https://github.com/helton/hbox/commit/465b5f758cd0b8fdf223acb206e8f4a4db673891))


## v0.2.1 (2024-05-03)

### Fix

* fix: update test.pypi.org env var ([`542a247`](https://github.com/helton/hbox/commit/542a247a3369fbfe19b73687dd63197824089e96))

### Unknown

* 0.2.1

Automatically generated by python-semantic-release ([`5285ce5`](https://github.com/helton/hbox/commit/5285ce58cfcbf89888c6ccbdafb96116d44d466a))


## v0.2.0 (2024-05-03)

### Chore

* chore: manually update version to match latest released version ([`1ca983b`](https://github.com/helton/hbox/commit/1ca983b9fc7add6b8e7ed81558e15934be1b8648))

### Ci

* ci: only publish if a release was generated ([`e944f64`](https://github.com/helton/hbox/commit/e944f64defab36167eef3bf7a85853b3be1bd4c6))

* ci: only publish if a release was generated ([`4f67afb`](https://github.com/helton/hbox/commit/4f67afbaf307599295e1dd120b8b9e50fee24673))

* ci: update semantic release configs ([`aba86a8`](https://github.com/helton/hbox/commit/aba86a8635bb20553e0fd59a5fedf19509024fa0))

* ci: disable semantic release until merge back with main ([`1667aa7`](https://github.com/helton/hbox/commit/1667aa79f0effa268303403daca40ac0dc80857b))

* ci: add semantic release ([`4eaa37a`](https://github.com/helton/hbox/commit/4eaa37ac46b7bbd7d53e8b6eb09e9f9bd10586bc))

### Feature

* feat: add semantic release to main branch only ([`122ec2f`](https://github.com/helton/hbox/commit/122ec2f64d5f167c7e75ecd89db16d3260c559cd))

### Fix

* fix: update version_toml to match current pyproject.toml structure ([`3af42b6`](https://github.com/helton/hbox/commit/3af42b6de5cc905ca00dc87cdba85cd093de671a))

* fix: update python-semantic-release/python-semantic-release to v8.3.0 to avoid issue #723 ([`ef8f722`](https://github.com/helton/hbox/commit/ef8f722607dd6e1021f2ee20a813555248430c68))

* fix: remove unused code and trigger new patch release ([`82ed4db`](https://github.com/helton/hbox/commit/82ed4dbe39cb91421b86e8bd5fc81380a7f1e2c0))

### Unknown

* 0.2.0

Automatically generated by python-semantic-release ([`afab6c6`](https://github.com/helton/hbox/commit/afab6c68f3106924782227274c655b2bbbb547cd))

* ciÃ: add develop as release branch ([`11fa8e7`](https://github.com/helton/hbox/commit/11fa8e7d7ef21b415c7083f81b510263ecf7d01d))


## v0.1.20 (2024-05-02)

### Chore

* chore: bump version to 0.1.20 ([`cb42e92`](https://github.com/helton/hbox/commit/cb42e92a3dcf99963282c298b48cc43c2082be16))

### Ci

* ci: install poetry before caching its deps ([`f724fbf`](https://github.com/helton/hbox/commit/f724fbf1977be27900f1d36dd0a139684f53b51b))

* ci: update actions to latest version + cache + simplify release ([`926f44a`](https://github.com/helton/hbox/commit/926f44a6b5db4be683a88c39cf65f0530ad602ec))


## v0.1.19 (2024-05-02)

### Chore

* chore: bump version to 0.1.19 ([`81369c2`](https://github.com/helton/hbox/commit/81369c29a6240dea1349772b46c2871b78869a3f))

* chore: update release message ([`522c136`](https://github.com/helton/hbox/commit/522c1365979dee1f53d74f168b33f76ede3f1eb8))


## v0.1.18 (2024-05-02)

### Chore

* chore: bump version to 0.1.18 ([`1cec259`](https://github.com/helton/hbox/commit/1cec2590b8cc30233ae50bd98a17fc2c7fcc15db))

* chore: add tag_name to Update Release Description step ([`d701b87`](https://github.com/helton/hbox/commit/d701b87f915a48654005f8f0f4ad088c89d01fd9))


## v0.1.17 (2024-05-02)

### Chore

* chore: bump version to 0.1.17 ([`eb1d406`](https://github.com/helton/hbox/commit/eb1d4061ee92c075867e403d5b49747681e50597))

* chore: add full asset path ([`9a8aa71`](https://github.com/helton/hbox/commit/9a8aa718db56d42e868f4f9f1e21a3310ca028e3))


## v0.1.16 (2024-05-02)

### Chore

* chore: bump version to 0.1.16 ([`be56269`](https://github.com/helton/hbox/commit/be562695dc18fb30ef0615d9da790306844beec7))

* chore: bump version to match latest release ([`d1997fa`](https://github.com/helton/hbox/commit/d1997fa164ec6ec75b739e5c55b3bedce40c3b0e))

* chore: release .tar.gz files instead of .zip to match poetry build
output ([`0afb43a`](https://github.com/helton/hbox/commit/0afb43aa36ac473bb4d134ea9810b4e52ae93fa8))


## v0.1.14 (2024-05-02)

### Chore

* chore: bump version to 0.1.14 ([`50d84d3`](https://github.com/helton/hbox/commit/50d84d399aa7a35322b5c9827830b1592af85c38))

* chore: rebuild before posting release assets ([`8c9459d`](https://github.com/helton/hbox/commit/8c9459de18d23c3e5bef2a858a28c261badf42b4))

* chore: bump version to 0.1.13 ([`f2f2e06`](https://github.com/helton/hbox/commit/f2f2e0641aa5a95911e4882a011962a8f9e23b2a))

* chore: update release version message ([`c6cd03b`](https://github.com/helton/hbox/commit/c6cd03b747ed6ebcecede93baccd00ca81513b79))

* chore: change tag and release assets with version number ([`2d26efe`](https://github.com/helton/hbox/commit/2d26efeb02a5e6cc2fc262c3fa8f58edbe0e2a04))

* chore: bump version to 0.1.12 ([`9bbeb28`](https://github.com/helton/hbox/commit/9bbeb28329e3729bbdf6b4d6b6c3edba42c87e39))

* chore: add permission to generate releases ([`6290575`](https://github.com/helton/hbox/commit/629057509823941803e22c2f0e27eb3a1645486d))

* chore: bump version to 0.1.11 ([`79f625f`](https://github.com/helton/hbox/commit/79f625ffc0412992524b757d4ec725b8d68bb681))

* chore: bump version to 0.1.10 ([`6fac3ef`](https://github.com/helton/hbox/commit/6fac3ef520dcc106ae8cbca764469127001511b2))

* chore: bump version to ([`9dc6ae3`](https://github.com/helton/hbox/commit/9dc6ae35a6ce896f23208b5c8a2b8d356fa60bb1))

* chore: update prod token + refactor create_pr ([`2449c2c`](https://github.com/helton/hbox/commit/2449c2c1d48251ebf3a264584323bb44d8753f14))

* chore: bump version to ([`ec3cf2d`](https://github.com/helton/hbox/commit/ec3cf2dc497a28bd4b415af1bf9494d309774a7d))

* chore: update PR creation from develop &gt; main ([`fb6b49a`](https://github.com/helton/hbox/commit/fb6b49a4d247dd8f29e5b4448604326f791794b7))

* chore: bump version to ([`827f800`](https://github.com/helton/hbox/commit/827f80069e03e9b5d2b8147f589a3bc6e8e19218))

* chore: update PR creation from develop &gt; main ([`22f778a`](https://github.com/helton/hbox/commit/22f778a7dfd192ad2c693f7e78f96d1db3889a7b))

* chore: bump version to ([`7fed13a`](https://github.com/helton/hbox/commit/7fed13a2927a25f709c2ec48ec2ffb390d573cde))

* chore: bump to existing version to avoid conflict ([`f3f5470`](https://github.com/helton/hbox/commit/f3f547036ea731e4fcfd344754a4b8b6272f18d5))

* chore: bump to existing version to avoid conflict ([`b1df10d`](https://github.com/helton/hbox/commit/b1df10dde12c0ec03103756d8fa6d72b23adeaf8))

* chore: bump to existing version to avoid conflictÃ ([`cb46f4d`](https://github.com/helton/hbox/commit/cb46f4dbf4e70af9d32e0093a7e61889cd8fe8d5))

* chore: update workflows ([`bc344b1`](https://github.com/helton/hbox/commit/bc344b1134b239f29b7dfef5dc0ad67da3bb20b5))

* chore: update workflows ([`a3b7ecc`](https://github.com/helton/hbox/commit/a3b7eccc8bbbb15c80b4696576345eb560af18a4))

* chore: update workflows ([`6a2eb20`](https://github.com/helton/hbox/commit/6a2eb20be3e1402371157c2b4b7678524ac589fa))

* chore: update workflows ([`39adb2f`](https://github.com/helton/hbox/commit/39adb2ffb184e9828d2ee9ff96c9067e1b14b1cf))

* chore: update workflows ([`de41017`](https://github.com/helton/hbox/commit/de41017e55900f5704480f6f1ad291273f29bb11))

* chore: update workflows ([`73c2cf6`](https://github.com/helton/hbox/commit/73c2cf6977a5c73d4e3cdd3f71bccbb54fe3afb8))

* chore: update workflows ([`7ab7ef3`](https://github.com/helton/hbox/commit/7ab7ef3ff1aa749099a013ab5a40c9c3f1c29bdf))

* chore: update workflows ([`1253e06`](https://github.com/helton/hbox/commit/1253e069a39f6c40337e8ddbb7247576808e873d))

* chore: update workflows ([`0f9725e`](https://github.com/helton/hbox/commit/0f9725e1c24b09d40dd57c6a28b0566579fb9d18))

* chore: update workflows ([`064793a`](https://github.com/helton/hbox/commit/064793a8ccb3f09398bc685dc99a5ce1c2d8263e))

* chore: update workflows ([`46de9d9`](https://github.com/helton/hbox/commit/46de9d9e0c3d16d7cf631a455fc91f529efd6c35))

* chore: update create_pr.py script ([`839a234`](https://github.com/helton/hbox/commit/839a23429b7209842b970aed31a4ba88cfa9ab51))

* chore: update create_pr.py script ([`118aa7b`](https://github.com/helton/hbox/commit/118aa7b4ee2363532cfc538fdaf47d16f61262e4))

* chore: update workflows ([`c5c11a8`](https://github.com/helton/hbox/commit/c5c11a88d08d9758c847670a7b74ed98197e6a1c))

* chore: update poetry install script ([`2a9aaac`](https://github.com/helton/hbox/commit/2a9aaac4d0e018ab019cfa40035188215a2522a3))

* chore: update poetry install script ([`fa87fff`](https://github.com/helton/hbox/commit/fa87ffff94e2d6a54505072a8a34fdd92059bcf4))

* chore: move workflow file ([`d7dd8f4`](https://github.com/helton/hbox/commit/d7dd8f4eaed075249585d146ec5cc0bc624c9de0))

* chore: bump version to 0.1.2 ([`80b570f`](https://github.com/helton/hbox/commit/80b570f4f1292df8050ab9da8baadc6c4c32b844))

* chore: get version from installed package ([`b03db38`](https://github.com/helton/hbox/commit/b03db38470bb85ec0b8e43865067929504bf5590))

* chore: update project name to hbox to avoid conflict with existing package ([`99d9882`](https://github.com/helton/hbox/commit/99d9882f523366d09efd3bf52dd72729906a4ac4))

### Documentation

* docs: add badges ([`ebd4e57`](https://github.com/helton/hbox/commit/ebd4e57bc4f77990f132dc0c04f2cac2641bfffa))

* docs: add installation ([`3e83b1d`](https://github.com/helton/hbox/commit/3e83b1dd7c9975956c2f22f8e6abd509df4a95a7))

* docs: update README.md ([`05d9922`](https://github.com/helton/hbox/commit/05d9922ab2a0e5f5a1d4587abca25f9982edd0ed))

### Fix

* fix: update bump version commit message to include version ([`b8b6c62`](https://github.com/helton/hbox/commit/b8b6c625d63c833b821eb9860a4057751385f603))

* fix: handles linux command execution and first time shims folder is created ([`bc4f3a7`](https://github.com/helton/hbox/commit/bc4f3a7ba651f20f5976791dfb9321178939b29c))

### Unknown

* choreÃ: remove unused validation in production env ([`1606653`](https://github.com/helton/hbox/commit/160665372ae1d41a85e97c0dc50b4e7850d4d28c))

* feature: create PR from feature to develop automatically ([`db4ce6e`](https://github.com/helton/hbox/commit/db4ce6e998b93b6e945cbafb37fac5eb5446e542))

* feature: create PR from feature to develop automatically ([`1753cc7`](https://github.com/helton/hbox/commit/1753cc71997371a01ddbeda006e83cc6a234f0f2))

* feature: add GitHub Actions workflow ([`c8670ec`](https://github.com/helton/hbox/commit/c8670ec8e4d29ccf3dd62cd3740a676a2fd5c518))

* feature: fully support debug messages and install, uninstall and set aliases ([`e16b2a7`](https://github.com/helton/hbox/commit/e16b2a7f62a4093f01c914d083827d9b7965cd0a))

* choreÃ: bump version to 0.1.1 ([`892ff92`](https://github.com/helton/hbox/commit/892ff9248bfd9bc8c921eb17269939b72c6b482c))

* feature: add kbox remove command ([`c5c8fb6`](https://github.com/helton/hbox/commit/c5c8fb65a78845c449cfe13583a0a8bea6591518))

* feature: first version ([`3955d0d`](https://github.com/helton/hbox/commit/3955d0d7ba3de5016553d63e34c53ed0ade1c4e9))
