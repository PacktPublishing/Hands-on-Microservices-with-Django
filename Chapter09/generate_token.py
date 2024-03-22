import jwt


def create_jwt(payload_to_encode):
    jwt_token = jwt.encode(payload=payload_to_encode,
                           key='<key_phrase>',
                           algorithm='HS256')
    return jwt_token


if __name__ == "__main__":
    print(create_jwt({"client_producer": "subscription_app"}))
    print(create_jwt({"service_producer": "match_address_worker"}))
