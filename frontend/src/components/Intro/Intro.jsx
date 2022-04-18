import React from "react";
import { Container, Row, Col,Button } from "react-bootstrap";
import intro from "../../Assets/intro_img.png";


export default function Intro() {
  return (
    <section>
        <Container fluid className="intro-section" id="home">
        <Container className="intro-content">
      <Row>
        <Col md={7} className="intro">
          <h1 style={{paddingBottom: 15 }} className="intro-first">
            조금 더
          </h1>
          <h1 style={{ paddingBottom: 15 }} className="intro-first">
            쉽게
          </h1>
          <h1 style={{ paddingBottom: 15 }} className="intro-first">
            편하게
          </h1>
          <h1 style={{ paddingBottom: 15 }} className="intro-first">
            알맞게
          </h1>
          <h1 className="into-second">
            <strong> 웹툰</strong>을 찾는 방법
          </h1>
            <div className="d-grid gap-2" 
                style={{
                    paddingLeft:10,
                    paddingBottom:65,
                    paddingTop:35,
                    width:200
                    }}>
                <Button  variant="dark" size="lg"  href="/Select">
                    Start?
                </Button>
            </div>
          </Col>
          <Col md={5} xs={12}>
          <img
            src={intro}
            alt="logo"
            className="img-fluid"
            style={{ maxHeight: "1000px"}}
          />
          </Col>
      </Row>
    </Container>
        </Container>
    </section>
    
  );
}