# yonks-ai

# 環境構築

```
docker-compose build
docker-compose up -d
```

# Sample

### curl
- userはマッチングを実施したいユーザー
- friendsはuserが登録している友達
- 各featureは，各項目が該当するか(0:非該当，1:該当)．
- featureの種類は任意．


| user_id | 映画 | ゲーム | アウドドア |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 2 | 1 | 1 | 1 |
| 3 | 0 | 0 | 0 |

```
curl -X 'POST' \
  'http://localhost:8000/euclidean/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user": {
    "user_id": 0,
    "feature": [
      0, 0, 0
    ]
  },
  "friends": [
    {
      "user_id": 1,
      "feature": [
        0, 1, 1
      ]
    },
    {
      "user_id": 2,
      "feature": [
        1, 1, 1
      ]
    },
    {
      "user_id": 3,
      "feature": [
        0, 0, 0
      ]
    }
  ]
}'
```


### Response body

- 左側がフレンドの user_id，右側が順位 (0が一番特徴が近い)

```
{
  "1": 2,
  "2": 0,
  "3": 1
}
```