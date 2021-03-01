import { clock } from "@xstream/core";

clock({ seconds: 3 })
  .filter(e => e % 2 != 0)
  .sink("even")
