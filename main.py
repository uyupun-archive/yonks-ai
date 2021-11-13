import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


def euclidean_distance(x, y):
    return np.linalg.norm((x[None, :] - y), axis=-1)


class Feature(BaseModel):
    user_id: int
    feature: List[int]


class User(BaseModel):
    user: Feature
    friends: List[Feature]


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/euclidean/")
def read_item(features: User):
    user = np.array(features.user.feature)
    friends = np.array([f.feature for f in features.friends])
    dist = euclidean_distance(user, friends).argsort().tolist()

    friends_id = [f.user_id for f in features.friends]
    result = dict(zip(friends_id, dist))

    return result
