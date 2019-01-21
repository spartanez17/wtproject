import React from "react";
import axios from "axios";
// import Articles from "../components/Article";
import CustomForm from "components/Form";

class ArticleList extends React.Component {
  state = {
    articles: {}
  };

  fetchWeather = (event, query, a, b, c) => {
    event.preventDefault();

    console.log(event);
    axios.get("http://127.0.0.1:8000/api/").then(res => {
      this.setState({
        articles: res.data
      });
    });
  };

  componentWillReceiveProps(newProps) {
    if (newProps.token) {
      this.fetchArticles();
    }
  }

  render() {
    return <CustomForm handleForm={this.fetchWeather} />;
  }
}

export default ArticleList;
