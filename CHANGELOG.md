## Main Functions
* `plot_trade`: first version of the function to plot trades. The function takes a PnL and the time series of the underlying, and plots both in two different subfigures. To learn more about how the function works, refer to the [docs](https://mpl-bsic.readthedocs.io/en/latest/)!
* `apply_bsic_style` 
    * __Multiple Axs__: Now works with multiple axes as parameters, as returned when calling `plt.subplots` with more than 1 subplot
    * __Sources__: now you can specify sources to be displayed at the bottom of the figure. By default, it specifies BSIC.
* `apply_bsic_logo`
    * Now the function works through an animation, which runs only once at the end.
* `check_figsize`: now it works properly, returning the recommended size for the plot, and prints any warning through the logging module. 

## Tests 

* Tests now work without showing the figure
* Implemented GH Actions to run tests on every PR

## Utils

* `add_fonts`: Function to check if the fonts are installed. If not, it installs them temporarily so that they can be used by `apply_bsic_style`
* `insert_animation`: appends an animation to the figure attribute `_bsic_animations`
* `run_animations`: forces the animations to run, so that they are correctly exported when it is not possible to render them (tests or when building docs)
* Utils are a module in itself and included in every release, so that functions can be imported from the main code

## Other

* __fonts__: garamond .ttf files were incorrect. I fixed them and put the correct files in the folder. 
* Updated [Docs](https://mpl-bsic.readthedocs.io/en/latest/) thoroughly, adding more examples and improving the way it saves and displays the plots.
* Animations are now stored in an attribute of the figure (`_bsic_animations`) as an list. When new animations are added they are appended to the list. See `insert_animation`


## List of the PRs merged
* Update README and License by @NotFrancee in https://github.com/NotFrancee/mpl_bsic/pull/4
* Add more thorough tests  by @NotFrancee in https://github.com/NotFrancee/mpl_bsic/pull/5
* Logo animation + fixed testing by @NotFrancee in https://github.com/NotFrancee/mpl_bsic/pull/6
* Fixed Fonts by @NotFrancee in https://github.com/NotFrancee/mpl_bsic/pull/7
* GitHub Actions and installing fonts in the system by @NotFrancee in https://github.com/NotFrancee/mpl_bsic/pull/8
* feat: moved logos outside the main project folder by @NotFrancee in https://github.com/NotFrancee/mpl_bsic/pull/9
* Fix utils imports and logo paths in prod  by @NotFrancee in https://github.com/NotFrancee/mpl_bsic/pull/10
* Fix animations to avoid lag while plotting by @NotFrancee in https://github.com/NotFrancee/mpl_bsic/pull/11
* feat: changed workflow filename and name by @NotFrancee in https://github.com/NotFrancee/mpl_bsic/pull/12
* apply_bsic_style with multiple axis by @NotFrancee in https://github.com/NotFrancee/mpl_bsic/pull/13
* Function to plot trades by @NotFrancee in https://github.com/NotFrancee/mpl_bsic/pull/14
* Improved `mpl_bsic.check_figsize()` by @NotFrancee in https://github.com/NotFrancee/mpl_bsic/pull/15
* Update Docs by @NotFrancee in https://github.com/NotFrancee/mpl_bsic/pull/16
* Added sources to plot when using apply_bsic_style by @NotFrancee in https://github.com/NotFrancee/mpl_bsic/pull/17


**Full Changelog**: https://github.com/NotFrancee/mpl_bsic/compare/1.1.6...1.2.0
## 1.3.1 (2024-04-23)

### Fix

- **dependencies**: fix dependencies for colab

## 1.3.0 (2024-02-24)

### Feat

- **export_figure**: function to export figure
- **style_excel**: style excel files, first version

### Fix

- **tests**: add xlsxwriter as dependency
- **apply_bsic_style**: when fig does not have suptitle
- **style_excel**: fix offset when title is None

### Refactor

- **__init__**: add export_figure to default exports
- **style_excel**: change function names to df_to_excel, style_excel_file
- **style_excel**: remove output_sheet parameter since redundant
- **style_excel**: remove unused _create_new_name function
- **debug-files**: move debug files to own directory and create debugconf.py for paths to work

## 1.2.2 (2023-12-01)

### Feat

- moved fonts inside mpl_bsic
- update pypi version

### Fix

- fonts path

## 1.2.1 (2023-12-01)

### Feat

- new test v
- updated testpypi version
- changelog
- docs for sources
- added sources and increased margin to make space
- savefig for debugging
- rcparams for saving the figure correctly (bbox and dpi)
- example for sources
- docs for sources parameter
- use run_animations from utils
- tests for when adding sources to the plot
- updated debug
- add sources to the plot when applying style
- version 1.2.0
- function to force animations to run
- test run_animations
- docs formatting
- docs
- example plots for apply_bsic_logo
- docs for plot_trade
- add version to title and docs for plot_trade
- import run_animations and set dpi to 900 by default
- esbonio confDir
- update testpypi version
- completed tests for check_figsize
- logging and improvements to check_figsize
- docs
- date formatting arguments in the main function
- _plot_entry_point with params specified in the main function
- include nominal pnl rather than cumul
- debug plot_trade
- first version of plot_trade
- weekly frequency
- apply style to fig suptitle
- tests for figures with multiple axs
- style plots with multiple axis
- changed workflow filename and name
- added debug file to quickly test the functions
- moved logos outside the main project folder
- add_fonts function
- add fonts even if not present in the system
- first commit poetry test workflow
- first version of test action
- added test group
- first commit poetry test workflow
- made logo animation and created util function
- test when there is a legend in the plot
- test logo on bottom left and bottom right
- added pragma: no cover for pytest-cov
- test when aspect_ratio and height are not specified
- removed .coverage from tracking
- tests for check_figsize
- test when logo gets called before style
- pytest-cov implementation
- testing logo (first version)
- flaky to run tests more than once
- about the projects in TOC
- about project section
- badges
- logo on header
- MIT license
- updated readme with header
- added logo to docs
- logo static file

### Fix

- finding package path
- reset the rcparams to save the figure correctly
- added bbox_inches tight to make sure sources are not cut out and reduces dpi
- updated baseline images to reflect sources
- add compare decorator to last test
- test floating point calculation and result
- calculation of width/height using aspect ratio
- run animation only once
- catch when animation has finished
- run animation only once at the end
- do not cache frames, fix for types
- don't cache frames and set delay between animations
- include utils to make it work in the final package
- moved logos back into main dir to work in prod
- force newer poetry version and python 3.12
- garamond fonts and font names
- enable testing without showing the figure
- handling of animation when testing functions
- removed unused file which caused conflicts when merging
- removed useless test
- align image
- installation hyperlink
- turn warnings into errors
- update readthedocs config

### Refactor

- always import baseline_save_fig
- compatibility with python 3.9
- specify version directly in docs/conf.py
- docstrings and removed old comments
- reorganize imports
- check if ax is a single axis, otherwise it is a list
- reorganize imports
- update to test multiple plots
- always import baseline_save_fig for better test development
- remove print statement
- position in animation function and added docstring
- unused ani event stop
- font directories and fonts names
- removed old test workflow
- changed gen_ann to gen_logo_annotation_box
- reorganize imports and comments
- remove plot_trade test (still WIP)

## 1.1.6 (2023-11-18)

## 1.1.5 (2023-11-16)
