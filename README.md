# 💻 Synonym API
An API for searching word synonyms. Only available in pt-BR.

## How it works
The data is scraped from the https://sinonimos.com.br web page and returned in a JSON formatted response.

### Stack
This is built using Python/Django and Django Rest Framework. You can check all the dependencies in [this file](pyproject.toml).

### Trying it out
Send a GET request to the endpoint `/api/v1/synonyms` with a search term as a query parameter, e.g.:

```http request
GET /api/v1/synonyms?query=adquirir
```

```json
{
    "query": "adquirir",
    "results": [
        {
            "meaning": "Passar a ter algo",
            "synonyms": [
                "comprar",
                "obter",
                "arranjar",
                "mercar"
            ]
        },
        {
            "meaning": "Conseguir",
            "synonyms": [
                "conseguir",
                "conquistar",
                "alcançar",
                "granjear",
                "atingir",
                "chegar",
                "ter",
                "atrair",
                "amanhar"
            ]
        },

        ...

    ]
}
```

Words can be interpreted in many ways. That's why we have a synonym set for each meaning of the searched term.

## License

This project is licensed under the [MIT License](LICENSE).
