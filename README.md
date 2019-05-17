# Repo for my blog: PythonforUndergradEngineers.com

 > [https://pythonforundergradengineers.com](https://pythonforundergradengineers.com)

Built with Python, [Pelican](https://docs.getpelican.com/en/stable/), and the [pelican-bootstrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3) theme. Deployed with [GitHub Pages](https://pages.github.com/)

 ## To build locally

 clone the repo

 ```
$ git clone https://github.com/ProfessorKazarinoff/staticsite.git
# update all the embedded git submodules
$ git submodule update --init --recursive
```

build the conda environment

```
> conda create -n staticsite python=3.7
> conda install -c conda-forge pelican==4.0.1 invoke==1.2.0
> conda install jupyter markdown==2.6.11   # some pelican plugins need mardown<3.0
> pip install pymdown-extensions
> conda activate staticsite
(staticsite)>
```

build the site and preview

```
(staticsite)> cd staticsite
(staticsite)> invoke build
(staticsite)> invoke serve
# view at localhost:8000
```

publish the site to GitHub Pages

```
(staticsite)> invoke publishsite
```


