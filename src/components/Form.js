import React from "react";
import { Container, Form, FormGroup, Input, Button } from "reactstrap";

class CustomForm extends React.Component {
  state = {
    query: ""
  };

  onFormSubmit = (event) => {
    event.preventDefault();
    this.props.handleSubmit(this.state.query)
  };

  render() {
    return (
      <div className="d-flex justify-content-start mw-100" style={{width:'550px'}}>
        <Form onSubmit={this.onFormSubmit} className="w-100">
          <FormGroup>
            <Input
              type="text"
              name="query"
              placeholder="City.."
              value={this.state.query}
              onChange={({ target: { value: query } }) =>
                this.setState({ query })
              }
            />
          </FormGroup>
          <Button className="mh-50" color="primary" type="submit">Get Weather!</Button>
        </Form>
      </div>
    );
  }
}

export default CustomForm;
