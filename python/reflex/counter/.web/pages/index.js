
/** @jsxImportSource @emotion/react */import { Fragment, useCallback, useContext } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Button, Heading, HStack } from "@chakra-ui/react"
import { EventLoopContext, StateContexts } from "/utils/context"
import { Event } from "/utils/state"
import "focus-visible/dist/focus-visible"
import NextHead from "next/head"



export function Button_96c7454569e2966bb8daeeb791a52464 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_7a4e8882198dad3c2b9a65dd4efed0c6 = useCallback((_e) => addEvents([Event("state.state.decrement", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_7a4e8882198dad3c2b9a65dd4efed0c6} sx={{"bg": "#fef2f2", "color": "#b91c1c", "borderRadius": "lg"}}>
  {`Decrement`}
</Button>
  )
}

export function Heading_16ccb9452a97c4059bfffd6f32d632f6 () {
  const state__state = useContext(StateContexts.state__state)


  return (
    <Heading sx={{"fontSize": "2em"}}>
  {state__state.count}
</Heading>
  )
}

export function Button_1507415da3e60988f7a7db84bc3ef15a () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_051be862d05745b9ead98f43abae2bac = useCallback((_e) => addEvents([Event("state.state.increment", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_051be862d05745b9ead98f43abae2bac} sx={{"bg": "#ecfdf5", "color": "#047857", "borderRadius": "lg"}}>
  {`Increment`}
</Button>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <HStack spacing={`1em`}>
  <Button_96c7454569e2966bb8daeeb791a52464/>
  <Heading_16ccb9452a97c4059bfffd6f32d632f6/>
  <Button_1507415da3e60988f7a7db84bc3ef15a/>
</HStack>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
