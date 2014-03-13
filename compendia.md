This is an example repo containing code from [ResearchCompendia 376](http://researchcompendia.org/compendia/376/).

For compendia code archives, one working assumption is that the archive will
have a directory structure like the following. This also conforms to usage
patterns in [Sumatra](http://pythonhosted.org/Sumatra/index.html) apart from
the results directory being named _compendiaoutput_ instead of _Data_.

```
project/
├── compendiaoutput/ is created by main
│   ├── ...          results that will get delivered to the webapp
├── default.json     default parameters and settings for a run
├── main             an executable that will run and consume the parameters and output to Data/
├── README           explains project structure and etc.
└── src/             nice if they nest source but they don't have to
```
