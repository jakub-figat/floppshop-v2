import styled from 'styled-components';
import { fontSize, colors } from 'styles/stylesConfig';
import { Link } from 'react-router-dom';
import backgroundTheme from 'assets/images/backgroundTheme.png';
import SVG from 'react-inlinesvg';

export const PageWrapper = styled.div`
  min-height: 100vh;
  min-width: 100vw;
  background-image: url(${backgroundTheme});
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const AuthBoxWrapper = styled.div`
  width: 30rem;
  height: auto;
  max-height: 50rem;
  overflow: auto;
  display: flex;
  background-color: ${colors.white};
  flex-direction: column;
  padding: 2rem 5rem 2rem 5rem;
  align-items: center;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
`;

export const HeadingWrapper = styled.div`
  text-align: center;
  margin-bottom: 2rem;
`;

export const FormHeading = styled.h2`
  font-size: ${fontSize.extraLarge};
`;

export const SubHeading = styled.p`
  font-size: ${fontSize.normal};
  margin-top: 0.9rem;
  color: ${colors.darkText};
`;

export const Form = styled.form`
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`;

export const SubmitButton = styled.button`
  height: 48px;
  width: 100%;
  margin-top: 1rem;
  display: inline-block;
  outline: none;
  cursor: pointer;
  font-size: ${fontSize.xSmall};
  border-radius: 7px;
  transition-property: background-color, border-color, color, box-shadow, filter;
  transition-duration: 0.3s;
  border: 1px solid transparent;
  letter-spacing: 2px;
  text-transform: uppercase;
  white-space: normal;
  font-weight: 700;
  text-align: center;
  padding: 16px 14px 18px;
  color: #fff;
  background-color: ${colors.mainGreen};
  :hover {
    background-color: ${colors.hoverGreen};
  }
`;

export const AuthInformationWrapper = styled.div`
  text-align: center;
  margin-top: 2rem;
`;

export const AccountMessage = styled.p`
  font-size: ${fontSize.small};
  color: ${colors.lightGray};
`;

export const RedirectLink = styled(Link)`
  text-decoration: none;
  color: ${colors.mainGreen};
  margin-top: 10px;
`;

export const Icon = styled(SVG)`
  min-width: 5rem;
  min-height: 5rem;
  max-width: 5rem;
  max-height: 5rem;
  margin-bottom: 1rem;

  & path {
    fill: ${colors.mainGreen};
  }
`;
