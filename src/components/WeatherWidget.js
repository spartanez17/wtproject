import React from "react";
import { Container, Row, Col } from "reactstrap";
import { unitSymbols } from "assets";

class WeatherWidget extends React.Component {
  render() {
    const { weather } = this.props;
    const {
      desc,
      icon,
      temp,
      humidity,
      windSpeed,
      date,
      country,
      city,
      units
    } = weather;
    console.log(units);

    return weather ? (
      <Container className="mw-100" style={{ height: "50vh" }}>
        <Row>
          <Col md={{ size: 6, offset: 3 }}>
            <p className="h3 font-weight-bold">{`Weather in ${city}, ${country}`}</p>
          </Col>
        </Row>
        <Row>
          <Col md={{ size: 5, offset: 2 }}>
            <h1>
              <img src={`http://openweathermap.org/img/w/${icon}.png`} alt="" />
              <span>{`${temp} ${unitSymbols[units]}`} </span>
            </h1>
          </Col>
          <Col >
          <ul>
            <li>{desc}</li>
            <li>{humidity}</li>
            <li>{windSpeed}</li>
          </ul>
          </Col>
        </Row>
      </Container>
    ) : (
      ""
    );
  }
}

export default WeatherWidget;
