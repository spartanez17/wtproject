import React from "react";
import {
  Form,
  FormGroup,
  Input,
  Button,
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
    const { query, units } = this.state;
    if (query) {
      this.props.handleSubmit(query, units);
    }
  };

  toggleUnits = units => {
    this.setState({ units });
  };

  render() {
    return (
      <div className="mw-100" style={{ margin: "6% auto", width: "550px" }}>
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
          <UncontrolledButtonDropdown direction="left" className="float-right">
            <DropdownToggle caret style={{ minWidth: "3.5em" }}>
              {this.state.units.symb}
            </DropdownToggle>
            <DropdownMenu className="" style={{ minWidth: "3em" }}>
              {Object.keys(units).map(key => {
                return (
                  <DropdownItem
                    key={key}
                    onClick={() => {
                      this.toggleUnits(units[key]);
                    }}
                  >
                    {units[key].symb}
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
