import { source, union, param } from "@xstream/core"
import { route_streams  } from "@xstream/gevent"

const streamReqA = source<number>("inA")
  .transform(e => ({ topic: "A", event: e }))

const streamReqB = source<number>("inB")
  .transform(e => ({ topic: "B", event: e }))

streamReqA.sink("reqA")
streamReqB.sink("reqB")

const res = param<string>("response-space")

union(streamReqA, streamReqB)
  .transform(e => ({
    topic: res + "/" + e.topic,
    event: e.event * 10
  }))
  .pipe(route_streams())
