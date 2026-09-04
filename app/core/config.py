from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "通用爬虫"
    app_env: str = "development"
    request_timeout: float = 20.0
    default_user_agent: str = "GeneralCrawlerBounty/0.1 (+compliant-public-data-collection)"
    output_path: str = "data/output/results.jsonl"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
