import React from "react";
import { Container, Row, Col } from "reactstrap";

class WeatherWidget extends React.Component {
  render() {
    const {
      desc,
      icon,
      temp,
      humidity,
      wind_speed,
      date,
      country,
      city,
      units,
      is_fetched
    } = this.props.weather;

    let formatedDate = formatDate(date);

    return (
      <Container className="rounded mw-100" style={{ height: "50vh" }}>
        <Row>
          <Col md={{ size: 6, offset: 3 }}>
            <p className="h3 font-weight-bold">{`Weather in ${city}, ${country}`}</p>
          </Col>
        </Row>
        <Row>
          <Col
            className="d-flex flex-column w-100 justify-content-center align-items-center"
            md={{ size: 5, offset: 2 }}
          >
            <h1>
              <img src={`http://openweathermap.org/img/w/${icon}.png`} alt="" />
              <span>{`${temp} ${units.symb}`} </span>
            </h1>
            <p className="text-secondary">{desc}</p>
            <p className="text-secondary">{formatedDate}</p>
          </Col>
          <Col className="d-flex flex-column w-100 justify-content-center align-items-start">
            <p className="h5 text-secondary">{`Humidity: ${humidity}%`}</p>
            <p className="h5 text-secondary">
              {`Wind: ${wind_speed} ${units.speed}`}
            </p>
            <p className="h6 text-secondary">{`just fetched: ${is_fetched}`}</p>
          </Col>
        </Row>
      </Container>
    );
  }
}
export default WeatherWidget;

const formatDate = timeStamp => {
  let dateObj = new Date(timeStamp * 1000);
  var options = {
    hour12: false,
    year: "numeric",
    day: "numeric",
    hour: "numeric",
    minute: "numeric",
    month: "long"
  };
  return dateObj.toLocaleTimeString("en-UN", options);
};
