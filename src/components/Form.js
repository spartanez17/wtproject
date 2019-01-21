import React from "react";
import { Form, Input, Button } from "reactstrap";

const CustomForm = props => (
  <div>
    <Form onSubmit={props.handleForm}>
    
      <Input placeholder="default" />

      <Button type="submit">Submit</Button>
    </Form>
  </div>
);

export default CustomForm;
