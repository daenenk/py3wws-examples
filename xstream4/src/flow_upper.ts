import { source } from "@xstream/core"
// import { to_upper } from "../ops/upper"

source<string>("hellotext")
//  .pipe(to_upper())
  .transform( e => e + "!")
  .sink("bigtext")