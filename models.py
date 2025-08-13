
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Dict, Any

class KPI(BaseModel):
    revenue: float
    ebitda: float
    gross_margin: float
    churn_rate: Optional[float] = None
    inventory_turns: Optional[float] = None
    utilization: Optional[float] = None

class PlanStep(BaseModel):
    week: int
    step: str
    owner_role: str = "Ops"

class Play(BaseModel):
    id: str
    type: Literal["pricing","retention","supply","utilization","claims","referrals"]
    title: str
    hypothesis: str
    uplift_usd: float
    uplift_pct: float
    confidence: Literal["low","medium","high"]
    complexity: Literal["low","medium","high"]
    assumptions: List[str]
    risks: List[str]
    plan: List[PlanStep]

class AnalysisResult(BaseModel):
    kpis: Dict[str, Any]
    plays: List[Play]
