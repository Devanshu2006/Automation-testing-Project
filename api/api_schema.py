class UserSchema:

    required_fields = {
        "id": int,
        "name": str,
        "email": str
    }

    @classmethod
    def validate(cls, data):

        for field, expected_type in cls.required_fields.items():

            assert field in data, (
                f"Missing field: {field}"
            )

            assert isinstance(data[field], expected_type), (
                f"{field} should be {expected_type.__name__}"
            )