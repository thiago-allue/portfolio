# Bootstrap Summary

Cheatsheet for bootstrap classes and snippets when using the bootstrap framework.

## Paragraph Classes

- text-muted, text-primary, text-success, text-info, text-warning, text-danger

## Backgrounds

- bg-primary, bg-success, bg-info, bg-warning, bg-danger

## Buttons

### Size

- btn-lg, btn-md, btn-sm, btn-xs

### Style

- btn-default, btn-primary, btn-success, btn-info, btn-warning, btn-danger, btn-link

## Tables

- table, table-striped, table-bordered, table-hover, table-condensed, table-responsive
- active, succcess, info, warning, danger

## Modal

**Preconditions**: `bootstrap.min.css` `jquery.min.css` `bootstrap.min.js`

```html
<button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#modalInfo">
Example
</button>
```

```html
<!-- Modal -->
<div class="modal fade" id="modalInfo" tabindex="-1" role="dialog" aria-labelledby="modalInfoLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title" id="modalInfoLabel">Modal title</h4>
            </div>
            <div class="modal-body">
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
            </div>
        </div>
    </div>
</div>
```