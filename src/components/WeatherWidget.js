import React from "react";
import { Container, Form, FormGroup, Input, Button } from "reactstrap";

class WeatherWidget extends React.Component {


  render() {
    const { weather } = this.props;
    return (
      <div
        className="d-flex justify-content-start mw-100"
        style={{ width: "550px" }}
      >
        {JSON.stringify(weather)}
      </div>
    );
  }
}

export default WeatherWidget;
