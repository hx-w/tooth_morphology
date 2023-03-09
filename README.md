<p align="center"><img src="https://imgbed.scubot.com/image/RoundCorner.png" width=138></p>
<h1 align="center">Tooth Morphology Collection</h1>
<p align="center"><strong>Collection of individual, feature-reserved and well-organized <em>3D Tooth models</em>.</strong></p>

<div align="center">

![repo-size](https://img.shields.io/github/repo-size/hx-w/tooth_morphology)
![commit-activity-weekly](https://img.shields.io/github/commit-activity/w/hx-w/tooth_morphology)
![dashboard](https://img.shields.io/github/actions/workflow/status/hx-w/tooth_morphology/DASHBOARD_UPDATER.yml?label=dashboard)
</div>



## Dashboard

![dataset summary](http://chat.scubot.com:7890/get/summary)

## Manual

### Workflow


### File Organization

```text
.
├── LICENSE
├── README.md
├── datasets  # dataset source
│   └── {{model type}}
│       └── {{model instance}}
|           |-- {{model file}}
│           └── {{model attachments}}
|
└── scripts   # scripts for maintenance
    ├── checker
    │   ├── check.py
    │   ├── fetcher.py
    │   ├── logger.py
    │   ├── rules.py
    │   └── wraper.py
    ├── dashboard
    │   ├── chart_bar.py
    │   ├── chart_bar_stack.py
    │   ├── dump.py
    │   ├── stats.py
    │   └── update.py
    ├── release.py
    └── requirements.txt
```

### Labels


### Branch strategy

- [master] projected.
- [data_{{name}}] models uploading, editing, deleting.
- [dev_{{name}}] scripts developing branch.
