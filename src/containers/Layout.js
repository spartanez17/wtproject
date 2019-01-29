import React from "react";
import {
  // Link,
  withRouter
} from "react-router-dom";
import { connect } from "react-redux";
import {
  Navbar,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  Container
} from "reactstrap";

import * as actions from "../store/actions/auth";
import { routes } from "assets";

class Layout extends React.Component {
  render() {
    const { isAuthenticated, username } = this.props;
    return (
      <div
        className="d-flex flex-column justify-content-between align-items-center"
        style={{ height: "100vh" }}
      >
        <header className="w-100 bg-dark" style={{ height: "10%" }}>
          <Container>
            <Navbar color="#FF0000" expand="md">
              <NavbarBrand href={routes.WEATHER}>
                <i class="fas fa-cloud fa-3x" />
              </NavbarBrand>
              <Nav className="align-items-center ml-auto" navbar>
                <NavItem>
                  {isAuthenticated ? (
                    <NavLink onClick={this.props.logout} href={routes.SIGN_IN}>
                      Sign out
                    </NavLink>
                  ) : (
                    <NavLink href={routes.SIGN_UP}>Sign up</NavLink>
                  )}
                </NavItem>
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
              </Nav>
            </Navbar>
          </Container>
        </header>
        <main className="mw-100" style={{ width: "1080px", height: "80%" }}>
          <Container>{this.props.children}</Container>
        </main>
        <footer>
          <NavLink
            className="float-right"
            href="https://github.com/spartanez17"
          >
            @Author
          </NavLink>
        </footer>
      </div>
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
