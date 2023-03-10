# Contributing

Feel free to submit your improvements and bug fixes. You can also propose your own program as a part of the shell, if you think it fits.

## Code

1. Before you open a PR containing substantial changes to already existing programs, please open a [Discussion](https://github.com/nwg-piotr/nwg-shell/discussions).
2. Half-baked PRs won't be merged:

    - **Make sure you don't introduce new bugs**. We already have enough bugs to fix.
    - **Make sure your work is finished** and needs no futher effort to be usable.
    - **Remember, that the project is intended for users of all skill levels**. Explain your new feature to the user. Add tooltips where needed. Update README / Wiki.
    - **Follow the existing coding style**. All the PRs like _I reformatted code with Black or whatever_ go directly to `/dev/null`, w/o further reading.

## Issues

Open an issue in appropriate GitHub repository to report a bug or request a feature.

## Translations

As of the nwg-shell-config 0.4.20 version, all the own (non-third party) shell components are supported by a common translation engine.
Since I don't really like gettext, which would be an overkill here anyway, I created a simple system based on the JSON format.
The base en_US lang, as well as pl_PL translation are provided together with each program. Other translations depend on contributors.

If you'd like to improve translations, or add your own, please click the translation button on the nwg-shell-config main screen:

![obraz](https://user-images.githubusercontent.com/20579136/224201486-2bf13d81-7b59-4df2-a7b8-e73e19144584.png)

This will open the nwg-shell-translate utility. Select an app and a language, create or edit phrases, use the "Export" button.
It will save a json file in your home directory, named like `app-name-ln_LN.json`. Then you may share the file as a [gist](https://gist.github.com),
or just send it to nwg.piotr@gmail.com. Thanks!

![obraz](https://user-images.githubusercontent.com/20579136/224203217-095ca616-9bdb-4957-b02c-f1ce521ee043.png)

*NOTE: All windows in the nwg-shell user interface are designed to fit 1/2 the screen width at 1920x1080 resolution. When typing phrases in your native language, pay attention that they are not too long. Use abbreviations when necessary.*
