## Hide/Show/Edit Columns

```python
dash_table.DataTable(
    columns=[
        {"name": ["", "Year"], "id": "year", "clearable": "first" },
        {"name": ["City", "Montreal"], "id": "montreal", "deletable": [False, True]},
        {"name": ["City", "Toronto"], "id": "toronto", "renamable": True },
        {"name": ["City", "Ottawa"], "id": "ottawa", "hideable": "last"},
        {"name": ["City", "Vancouver"], "id": "vancouver", "clearable": True, "renamable": True, "hideable": True, "deletable": True },
        {"name": ["Climate", "Temperature"], "id": "temp"},
        {"name": ["Climate", "Humidity"], "id": "humidity"},
    ],
    data=[
        {
            "year": i,
            "montreal": i * 10,
            "toronto": i * 100,
            "ottawa": i * -1,
            "vancouver": i * -10,
            "temp": i * -100,
            "humidity": i * 5,
        }
        for i in range(10)
    ],
    css=[
        {"selector": ".column-header--delete svg", "rule": 'display: "none"'},
        {"selector": ".column-header--delete::before", "rule": 'content: "X"'}
    ]
)
```

## Export data

```python
dash_table.DataTable(
    columns=[
        {"name": ["", "Year"], "id": "year" },
        {"name": ["City", "Montreal"], "id": "montreal", "deletable": [False, True]},
        {"name": ["City", "Toronto"], "id": "toronto", "renamable": True },
        {"name": ["City", "Ottawa"], "id": "ottawa", "hideable": "last"},
        {"name": ["City", "Vancouver"], "id": "vancouver"},
        {"name": ["Climate", "Temperature"], "id": "temp"},
        {"name": ["Climate", "Humidity"], "id": "humidity"},
    ],
    data=[
        {
            "year": i,
            "montreal": i * 10,
            "toronto": i * 100,
            "ottawa": i * -1,
            "vancouver": i * -10,
            "temp": i * -100,
            "humidity": i * 5,
        }
        for i in range(10)
    ],
    export_format='xlsx',
    export_headers='display',
    merge_duplicate_headers=True
)
```