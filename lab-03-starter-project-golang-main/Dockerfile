FROM golang:alpine as build

WORKDIR /app

COPY . .

RUN go build -o build/fizzbuzz

FROM gcr.io/distroless/static-debian11

COPY --from=build /app/build/fizzbuzz /

COPY --from=build /app/templates/index.html /templates/

CMD ["/fizzbuzz", "serve"]