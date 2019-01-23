import React from "react";
import {
  Container,
  Form,
  FormGroup,
  Input,
  Button,
  Dropdown,
  UncontrolledButtonDropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem
} from "reactstrap";

import { units } from "assets";

class CustomForm extends React.Component {
  state = {
    query: "",
    dropdownOpen: false,
    units: units.CELSIUS
  };

  onFormSubmit = event => {
    event.preventDefault();
    const {query, units} = this.state
    if (query) {
      this.props.handleSubmit({
        query,
        units
      });
    }
  };

  toggleUnits = units => {
    this.setState({ units });
  };

  render() {
    return (
      <div
        className="d-flex justify-content-start mw-100"
        style={{ width: "550px" }}
      >
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
          <Button className="mh-50" color="primary" type="submit">
            Get Weather!
          </Button>
          <UncontrolledButtonDropdown className="float-right w-25">
            <DropdownToggle caret>{this.state.units}</DropdownToggle>
            <DropdownMenu>
              {Object.keys(units).map(key => {
                return (
                  <DropdownItem
                    onClick={() => {
                      this.toggleUnits(units[key]);
                    }}
                  >
                    {key}
                  </DropdownItem>
                );
              })}
            </DropdownMenu>
          </UncontrolledButtonDropdown>
        </Form>
      </div>
    );
  }
}

export default CustomForm;
