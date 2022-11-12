# PDF-PageRoation-Flask-RestAPI

Rotate pdf specific page using this python application by simply providing file path, angle of rotation and page number.

```
Get Request
http://127.0.0.1:5000/rotate?file_path=C:/Users/mynam/Desktop/FlaskAssignment/test.pdf&angle_of_rotation=90&page_number=2
```

```
Response on successful rotation
{
    "new_file_path": "C:/Users/mynam/Desktop/FlaskAssignment/test_new_90_rotated_file_at_page_number_2.pdf",
    "old_file": "C:/Users/mynam/Desktop/FlaskAssignment/test.pdf",
    "angle_of_rotation": 90,
    "page_number": 2
}
```

If angle of rotation is not multiple of 90, response
```
{
    "error": "angle_of_rotation is not valid! Should be multiple of 90"
}
```
If page_number if out of domain
```
{
    "error": "page_number is not valid"
}
```
