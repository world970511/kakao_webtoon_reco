import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import {
  AiFillGithub,
  AiOutlineTwitter,
  AiFillInstagram,
} from "react-icons/ai";


function Footer() {
  let date = new Date();
  let year = date.getFullYear();
  return (
    <Container fluid className="footer">
      <Row>
      <Col md="12" className="footer-body">
            <h5>Find us</h5>
                <a
                href="https://github.com/world970511"
                target="_blank"
                rel="noreferrer"
                style={{color:"#c4c4c4"}}
                >
                Naeun<AiFillGithub />
                </a>
                {" "}
                <a
                href="https://github.com/hjlim7831"
                target="_blank"
                rel="noreferrer"
                style={{color:"#c4c4c4"}}
                >
                Hyejin<AiFillGithub />
                </a>

        </Col>
        <Col md="12" className="footer-copywright">
          <h5>Copyright © {year} Naeun and Hyejin</h5>
        </Col>
      </Row>
    </Container>
  );
}

export default Footer;