<p align="center"><img src="https://imgbed.scubot.com/image/RoundCorner_1.png" width=138></p>

<p><h2 align="center">
Tooth Morphology Collection
</h2></p>

<div align="center">

![repo-size](https://img.shields.io/github/repo-size/hx-w/tooth_morphology?style=for-the-badge&logo=starship&color=C9CBFF&logoColor=D9E0EE&labelColor=302D41")
![commit-activity-weekly](https://img.shields.io/github/commit-activity/w/hx-w/tooth_morphology?style=for-the-badge&logo=github&color=F2CDCD&logoColor=D9E0EE&labelColor=302D41")
![dashboard](https://img.shields.io/github/actions/workflow/status/hx-w/tooth_morphology/DASHBOARD_UPDATER.yml?label=dashboard&style=for-the-badge&logo=gitbook&color=B5E8E0&logoColor=D9E0EE&labelColor=302D41")
</div>

<h4 align="center"><strong>
A collection of individual, feature-reserved and well-organized <em>3D Tooth models</em>.
<strong></h4>

&nbsp;

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

<table border="0">
<tr>
<td>
<p align="center"><strong>Summary</strong></p>
<p align="center"><a href="http://chat.scubot.com:7890/get/summary-?redirect=true" target="view_window"> [source]  </a> </p>
</td>
<td><img src=http://chat.scubot.com:7890/get/summary-?redirect=false width=600/></td>
</tr>
<tr>
<td>
<p align="center"><strong>Updates</strong></p>
<p align="center"><a href="http://chat.scubot.com:7890/get/diff-?redirect=true" target="view_window"> [source] </a> </p>
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

- [master] protected.
- [data_{{name}}] models uploading, editing, deleting.
- [dev_{{name}}] scripts developing branch.
