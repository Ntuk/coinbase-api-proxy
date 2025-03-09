const { build } = require('esbuild');
const { copyFile } = require('fs/promises');

async function runBuild() {
  // Bundle the TypeScript code
  await build({
    entryPoints: ['src/index.ts'],
    bundle: true,
    minify: true,
    platform: 'node',
    target: 'node18',
    outfile: 'dist/index.js',
    external: ['aws-sdk']
  });

  console.log('Build completed successfully!');
}

runBuild().catch(e => {
  console.error('Build failed:', e);
  process.exit(1);
});
