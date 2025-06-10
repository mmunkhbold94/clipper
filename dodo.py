def task_generate_models() -> dict:
    """Generate Pydantic models from OpenAPI spec."""
    return {
        "actions": [
            "datamodel-codegen "
            "--input openapi/openapi.yaml "
            "--output clipper/models/generated.py "
            "--input-file-type openapi "
            "--target-python-version 3.11 "
            "--use-generic-container-types "
            "--use-union-operator "
            "--enable-faux-immutability"
        ],
        "file_dep": ["openapi/openapi.yaml"],
        "targets": ["clipper/models/generated.py"],
    }