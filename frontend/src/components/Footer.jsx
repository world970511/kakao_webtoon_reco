import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import {
  AiFillGithub,
  AiOutlineTwitter,
  AiFillInstagram,
} from "react-icons/ai";
import { FaLinkedinIn } from "react-icons/fa";

function Footer() {
  let date = new Date();
  let year = date.getFullYear();
  return (
    <Container fluid className="footer">
      <Row>
        <Col md="12" className="footer-copywright">
          <h5>Copyright © {year} Naeun and Hyejin</h5>
        </Col>
        <Col md="12" className="footer-body">
            <h5>Find us {" "}
            <a
                href="https://github.com/world970511/kakao_webtoon_reco"
                target="_blank"
                rel="noreferrer"
                style={{color:"white"}}
            >
                <AiFillGithub />
            </a>
            </h5>
        </Col>
      </Row>
    </Container>
  );
}

export default Footer;