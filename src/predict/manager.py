from .schema import PredictRequest, PredictResponseFactory, PredictResponse

class PredictManager():

    @classmethod
    async def predict(cls, predict_request: PredictRequest) -> PredictResponse:
        # TODO: Implement prediction
        return PredictResponseFactory.predict_from_price(100.0)