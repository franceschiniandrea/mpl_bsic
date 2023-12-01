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