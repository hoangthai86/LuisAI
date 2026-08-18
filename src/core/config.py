from dataclasses import dataclass, field


@dataclass
class AIProviderConfig:
    name: str
    enabled: bool = True
    provider_type: str = "remote"
    model: str | None = None
    timeout_seconds: int = 60


@dataclass
class LuisAIConfig:
    name: str = "LuisAI"
    version: str = "0.1.0"

    # Các AI có thể chạy song song
    ai_providers: list[AIProviderConfig] = field(
        default_factory=lambda: [
            AIProviderConfig(
                name="OpenAI",
                enabled=True,
                provider_type="remote",
            ),
            AIProviderConfig(
                name="LocalAI",
                enabled=False,
                provider_type="local",
            ),
        ]
    )

    # Quy trình xử lý
    parallel_ai: bool = True
    enable_critics: bool = True
    enable_final_synthesis: bool = True

    # Phân tích tài chính
    enable_fundamental_analysis: bool = True
    enable_technical_analysis: bool = True
    enable_valuation: bool = True
    enable_quant_analysis: bool = True

    # Phân tích nâng cao
    enable_behavioral_analysis: bool = True
    enable_econometrics: bool = True
    enable_statistics: bool = True
    enable_probability: bool = True

    # Quản trị rủi ro và danh mục
    enable_risk_management: bool = True
    enable_portfolio_management: bool = True

    # AI chỉ đưa ra quyết định mang tính tham khảo
    advisory_only: bool = True
    require_uncertainty: bool = True

    # Không cho phép hệ thống tự tuyên bố chắc chắn tuyệt đối
    max_confidence: float = 0.95


DEFAULT_CONFIG = LuisAIConfig()