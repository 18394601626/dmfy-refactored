from pydantic_settings import BaseSettings, SettingsConfigDict
class HereticSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="HERETIC_")
    model_name_or_path: str
    output_dir: str = "ablated_loras"