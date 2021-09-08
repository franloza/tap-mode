"""Mode Authentication."""


from singer_sdk.authenticators import SimpleAuthenticator


class ModeAuthenticator(SimpleAuthenticator):
    """Authenticator class for Mode."""

    @classmethod
    def create_for_stream(cls, stream) -> "ModeAuthenticator":
        return cls(
            stream=stream,
            auth_headers={
                "Authorization": f"Bearer {stream.config.get('auth_token')}"
            }
        )
