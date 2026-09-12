import neo4j from 'neo4j-driver';
const driver = neo4j.driver('bolt://100.87.214.70:7687', neo4j.auth.basic('neo4j', 'changeme'));
const session = driver.session();
async function main() {
  const result = await session.run('MATCH (v:Venture) RETURN v LIMIT 1');
  console.log(result.records[0].get('v').properties);
  await session.close();
  await driver.close();
}
main();
