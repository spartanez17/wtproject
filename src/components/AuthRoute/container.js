import { connect } from "react-redux";
import AuthRoute from "../AuthRoute";

const mapStateToProps = state => ({
  token: state.token
});

export default connect(mapStateToProps)(AuthRoute);