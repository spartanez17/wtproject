import React from "react";
import { Link, withRouter } from "react-router-dom";
import { connect } from "react-redux";
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  UncontrolledDropdown,
  Alert,
  Container,
  Row,
  Col
} from "reactstrap";

import * as actions from "../store/actions/auth";
import { routes } from "assets";

class Layout extends React.Component {
  render() {
    const { isAuthenticated, username } = this.props;
    return (
      <Container
        className="d-flex flex-column justify-content-between"
        style={{ height: "100vh" }}
        fluid
      >
        <header style={{ height: "10vh" }}>
          <Navbar color="#FF0000" expand="md">
            <NavbarBrand href={routes.WEATHER}>
              <i size="9px" class="fas fa-cloud fa-2x" />
            </NavbarBrand>
            <NavbarToggler onClick={this.toggle} />
            <Nav className="ml-auto" navbar>
              <NavItem>
                {isAuthenticated ? (
                  <NavLink
                    disabled
                    href=""
                  >{`Signed in as ${username}`}</NavLink>
                ) : (
                  <NavLink href={routes.SIGN_IN}>Sign in</NavLink>
                )}
              </NavItem>
              <NavItem>
                {isAuthenticated ? (
                  <NavLink onClick={this.props.logout} href={routes.SIGN_IN}>
                    Sign out
                  </NavLink>
                ) : (
                  <NavLink href={routes.SIGN_UP}>Sign up</NavLink>
                )}
              </NavItem>
            </Nav>
          </Navbar>
        </header>
        <main style={{ padding: 24, height: "80vh" }}>
          {this.props.children}
        </main>
        <footer>
          <NavLink
            className="float-right"
            href="https://github.com/spartanez17"
          >
            @Author
          </NavLink>
        </footer>
      </Container>
    );
  }
}

const mapDispatchToProps = dispatch => {
  return {
    logout: () => dispatch(actions.logout())
  };
};

const mapStateToProps = state => {
  return {
    username: state.username
  };
};

export default withRouter(
  connect(
    mapStateToProps,
    mapDispatchToProps
  )(Layout)
);
