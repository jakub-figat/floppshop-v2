import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { ApplicationRoutes } from 'config/variables';

import NotFoundPage from 'common/pages/NotFoundPage';
import MainPage from 'common/pages/MainPage';
import AuthenticationPage from 'common/pages/AuthenticationPage';

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path={ApplicationRoutes.login} element={<AuthenticationPage />} />
        <Route path={ApplicationRoutes.main} element={<MainPage />} />
        <Route path={ApplicationRoutes.notFound} element={<NotFoundPage />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;
