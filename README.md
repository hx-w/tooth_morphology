<p align="center"><img src="https://imgbed.scubot.com/image/RoundCorner_1.png" width=138></p>
<h1 align="center">Tooth Morphology Collection</h1>
<p align="center"><strong>Collection of individual, feature-reserved and well-organized <em>3D Tooth models</em>.</strong></p>

<div align="center">

![repo-size](https://img.shields.io/github/repo-size/hx-w/tooth_morphology)
![commit-activity-weekly](https://img.shields.io/github/commit-activity/w/hx-w/tooth_morphology)
![dashboard](https://img.shields.io/github/actions/workflow/status/hx-w/tooth_morphology/DASHBOARD_UPDATER.yml?label=dashboard)
</div>



## Dashboard
<!-- <table>
    <tr>
        <td><p align="center">Summary</p>
        </td>
        <td><p align="center">Updates</p>
        </td>
    </tr>
    <tr>
        <td><img src=http://chat.scubot.com:7890/get/summary- width=600/></td>
        <td><img src=http://chat.scubot.com:7890/get/diff- width=600/></td>
    </tr>
</table> -->

<table border="1">
<tr>
<td>
<p align="center"><strong>Summary</strong></p>
<p align="center"><a href="http://chat.scubot.com:7890/get/summary-?redirect=true" target="_blank"> [source]  </a> </p>
</td>
<td><img src=http://chat.scubot.com:7890/get/summary-?redirect=false width=600/></td>
</tr>
<tr>
<td>
<p align="center"><strong>Updates</strong></p>
<p align="center"><a href="http://chat.scubot.com:7890/get/diff-?redirect=true" target="_blank"> [source] </a> </p>
</td>
<td><img src=http://chat.scubot.com:7890/get/diff-?redirect=false width=600/></td>
</tr>
</table>

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
|           |── {{model file}}
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
