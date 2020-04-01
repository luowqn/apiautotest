def test_%(seq1)d_ %(seq2)d(self, bodyfile='%{bodyfile}s', bodyargs= %{bodyargs}s, url = '%{url}s',no=%{no}d
   method = '%{method}s', respOps = [ %{respOps}s], respAssertions = %{respAssertions}s):
    global gVars
    self._testMethodDoc = '%(testMethodDoc)s'
    vars = {}

    for var in respOps:
        temp = var.split(':')[-1]
        if 'get' in var:
            vars[var.split('.')[-1]] = gVars.get(var)
        if 'filter' in var:
            pass

    vars.update(**bodyargs)
    body = RequestSDK.buidBody(bodyfile, vars)
    resp = RequestSDK.sendReq(self.socketfd, url, method, json=body)
    if resp.status_code == 200:
        respJson = json.loads(resp.text)
        # 提取变量
        if "0" == respJson.get("code"):
            for respExtract in respExtracts:
                vals = re.findall('\"' + respExtract + '\":\"(.*?)\"', resp.text, re.M | re.I)
                gVars[str(no) + '.' + respExtract] = vals[0]
        # 断言
        for respAssertion in respAssertions:
            self.assertIn(respAssertion, resp.text)