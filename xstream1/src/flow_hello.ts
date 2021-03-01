import { source  } from "@xstream/core"

source<string>("text")
  .transform( e => "hello " + e )
  .sink("hellotext")
